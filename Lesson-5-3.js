var basket = {
    content: [
        {
            id: 1,
            name: "apple",
            price: 10,
            quantity: 5
        },
        {
            id: 2,
            name: "orange",
            price: 30,
            quantity: 2
        },
        {
            id: 3,
            name: "tomato",
            price: 20,
            quantity: 4
        },
    ],

    TotalItems() {
        total = 0;
        for (i = 0; i < basket.content.length; i++) {
            total = total + basket.content[i].quantity
        }
        return (total)
    },

    TotalBasketPrice() {
        total = 0;
        for (i = 0; i < basket.content.length; i++) {
            total = total + basket.content[i].price * basket.content[i].quantity
        }
        return (total)
    }
}


function showBasket() {
    n = basket.TotalItems();
    listItems();
    total = document.createElement('span');
    document.getElementById("basket").appendChild(total);
    if (n > 0) {
        total.innerText = "ИТОГО в вашей корзине " + n + " товаров на сумму " + basket.TotalBasketPrice() + " рублей";
    }
    else {
        total.innerText = "Ваша корзина пуста";
    }

}

function listItems() {
    basketContainer = document.getElementById("basket");
    for (i = 0; i < basket.content.length; i++) {
        itemDiv = document.createElement('div');
        basketContainer.appendChild(itemDiv);
        nameDiv = document.createElement('div');
        itemDiv.appendChild(nameDiv);
        nameDiv.innerText = "Наименование: " + basket.content[i].name;
        priceDiv = document.createElement('div');
        itemDiv.appendChild(priceDiv);
        priceDiv.innerText = "Цена: " + basket.content[i].price;
        quantityDiv = document.createElement('div');
        itemDiv.appendChild(quantityDiv);
        quantityDiv.innerText = "Количество: " + basket.content[i].quantity;
    }

}