package demo;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class Invoice {
    private final String orderId;
    private final List<BigDecimal> amounts = new ArrayList<>();

    public Invoice(String orderId) {
        this.orderId = orderId;
    }

    public void addLine(BigDecimal amount) {
        amounts.add(amount);
    }

    public BigDecimal total() {
        return amounts.stream().reduce(BigDecimal.ZERO, BigDecimal::add);
    }

    public String getOrderId() {
        return orderId;
    }
}
