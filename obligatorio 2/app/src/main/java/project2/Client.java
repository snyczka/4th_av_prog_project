package project2;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Client {

    private final Integer id;
    private String userName;
    private String email;
    private float wallet;
    private List<Integer[]> shoppingCart;
    private Integer priorityLevel;

    public Client(Integer id, String userName, String email) {
        this.id = id;
        this.userName = userName;
        this.email = email;
        this.wallet = 0f;
        this.shoppingCart = new ArrayList<>();
        this.priorityLevel = 5;
    }

    public Client(Integer id, String userName, String email, float wallet) {
        this.id = id;
        this.userName = userName;
        this.email = email;
        this.wallet = wallet;
        this.shoppingCart = new ArrayList<>();
        this.priorityLevel = 5;
    }

    public Client(Integer id, String userName, String email, float wallet, Integer priorityLevel) {
        this.id = id;
        this.email = email;
        this.wallet = wallet;
        this.shoppingCart = new ArrayList<>();
        this.priorityLevel = priorityLevel;
    }



    public float getWallet() {
        return this.wallet;
    }

    public void setWallet(float wallet) {
        this.wallet = wallet;
    }


    public Integer getId() {
        return this.id;
    }

    public String getUserName() {
        return this.userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getEmail() {
        return this.email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public List<Integer[]> getShoppingCart() {
        return this.shoppingCart;
    }

    public void setShoppingCart(List<Integer[]> shoppingCart) {
        this.shoppingCart = shoppingCart;
    }

    public Integer getPriorityLevel() {
        return this.priorityLevel;
    }

    public void setPriorityLevel(Integer priorityLevel) {
        this.priorityLevel = priorityLevel;
    }



    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof Client)) {
            return false;
        }
        Client client = (Client) o;
        return Objects.equals(id, client.id) && Objects.equals(email, client.email) && Objects.equals(shoppingCart, client.shoppingCart) && Objects.equals(priorityLevel, client.priorityLevel);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.id);
    }
    

    
}
