from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Fraud Graph Detector API")

# 1. Graph and Cycle Detection Engine
class TransactionGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_transaction(self, sender: str, receiver: str, amount: float):
        if sender not in self.adjacency_list:
            self.adjacency_list[sender] = []
        self.adjacency_list[sender].append({
            "to": receiver,
            "amount": amount
        })

    def _dfs(self, node, visited, recursion_stack):
        visited.add(node)
        recursion_stack.add(node)

        if node in self.adjacency_list:
            for edge in self.adjacency_list[node]:
                neighbor = edge["to"]
                if neighbor not in visited:
                    if self._dfs(neighbor, visited, recursion_stack):
                        return True
                elif neighbor in recursion_stack:
                    return True

        recursion_stack.remove(node)
        return False

    def detect_fraudulent_cycles(self) -> bool:
        visited = set()
        recursion_stack = set()
        for node in self.adjacency_list:
            if node not in visited:
                if self._dfs(node, visited, recursion_stack):
                    return True
        return False

# 2. Pydantic Models for API Validation
class Transaction(BaseModel):
    sender: str
    receiver: str
    amount: float

class TransactionBatch(BaseModel):
    transactions: List[Transaction]

# 3. API Endpoint
@app.post("/check-transactions")
def check_transactions(batch: TransactionBatch):
    graph = TransactionGraph()
    
    for tx in batch.transactions:
        graph.add_transaction(tx.sender, tx.receiver, tx.amount)
        
    is_fraudulent = graph.detect_fraudulent_cycles()
    
    if is_fraudulent:
        return {
            "status": "ALERT",
            "message": "Suspicious circular money flow (money laundering loop) detected!",
            "fraud_detected": True
        }
    else:
        return {
            "status": "SAFE",
            "message": "No circular money flows found in this batch.",
            "fraud_detected": False
        }