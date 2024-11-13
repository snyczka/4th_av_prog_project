package project2.transactions;


import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

import project2.Client;
import project2.Product;

public class CartTxTests {

    @Test void correctTransaction() {
        Client buyer = new Client(1, "J", "j@gm.c", 2000f);
        Product pro = new Product(0, "Ball", 2f, 2);
        CartTx classUnderTest = new CartTx(buyer, pro, 2);
        classUnderTest.run();
        assertEquals(0, pro.getStock(), "Success!");
    }
}
