package project2;

import java.util.List;
import java.util.UUID;

public class CheckoutReceip implements Comparable<CheckoutReceip>{
    
    private final UUID receipId;
    private final Integer userId;
    private final List<Integer[]> shoppingCart;
    private final Integer priority;


    public CheckoutReceip(Integer userId, List<Integer[]> shoppingCart, Integer priority) {
        this.receipId = UUID.randomUUID();
        this.userId = userId;
        this.shoppingCart = shoppingCart;
        this.priority = priority;
    }


    public UUID getReceipId() {
        return this.receipId;
    }


    public Integer getUserId() {
        return this.userId;
    }

    public List<Integer[]> getShoppingCart() {
        return this.shoppingCart;
    }


    public Integer getPriority() {
        return this.priority;
    }


    @Override
    public int compareTo(CheckoutReceip o) {
        return Integer.compare(this.priority, o.getPriority());
    }


}
