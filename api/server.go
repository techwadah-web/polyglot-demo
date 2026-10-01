package api

import (
	"encoding/json"
	"net/http"
)

// OrderRequest is the body of POST /orders.
type OrderRequest struct {
	ISBN     string `json:"isbn"`
	Quantity int    `json:"quantity"`
}

// OrderResponse is returned when an order is accepted.
type OrderResponse struct {
	OrderID string `json:"order_id"`
	Status  string `json:"status"`
}

// Reserver reserves stock for an order.
type Reserver interface {
	Reserve(isbn string, quantity int) error
}

// HandleOrder accepts an order and reserves stock.
func HandleOrder(stock Reserver) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		var req OrderRequest
		if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
			http.Error(w, "invalid body", http.StatusBadRequest)
			return
		}
		if err := stock.Reserve(req.ISBN, req.Quantity); err != nil {
			http.Error(w, err.Error(), http.StatusConflict)
			return
		}
		writeJSON(w, OrderResponse{OrderID: newOrderID(), Status: "reserved"})
	}
}

func writeJSON(w http.ResponseWriter, v any) {
	w.Header().Set("Content-Type", "application/json")
	_ = json.NewEncoder(w).Encode(v)
}

func newOrderID() string {
	return "ord_demo"
}
