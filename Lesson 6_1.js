function test() {
    alert('item')
};

const basket = {
    content: [],

    addItems(e) {
        if (basket.content[e.target.value] == undefined) {
            basket.content[e.target.value] = 1
        }
        else { basket.content[e.target.value]++ };
        // console.log(Object.values(basket.content))
        console.log((basket.content[e.target.value])); // quantity of each
        console.log(basket.content.length);
        basket.showBasketTotal();
    },

    showBasketTotal() {
        n = basket.content.length;
        total = document.getElementById("totalspan")
        if (total == undefined) {
            total = document.createElement('span');
            total.id = "totalspan";
            document.getElementById("basket").appendChild(total);
        };


        if (basket.content.length > 0) {
            total.innerText = "ИТОГО в вашей корзине " + basket.TotalItems() + " товаров на сумму " + basket.TotalBasketPrice() + " рублей";
        }
        else {
            total.innerText = "Ваша корзина пуста";
        }
    },

    TotalItems() {
        var key = 0;
        total = 0;
        for (i = 0; i < basket.content.length; i++) {
            key = Object.keys(basket.content)[i];
            total = total + basket.content[key];
        }
        return (total)
    },

    TotalBasketPrice() {
        total = 0;
        for (i = 0; i < basket.content.length; i++) {
            total = total + basket.content[i] * catalogue.content[i].price
        }
        return (total)
    }
}

const catalogue = {
    content: [
        {
            id: 1,
            name: "apple",
            price: 10
        },

        {
            id: 2,
            name: "orange",
            price: 30
        },

        {
            id: 3,
            name: "tomato",
            price: 20
        }
    ],

    listItems() {
        catalogueContainer = document.getElementById("catalogue");
        for (i = 0; i < catalogue.content.length; i++) {
            itemDiv = document.createElement('div');
            catalogueContainer.appendChild(itemDiv);
            nameDiv = document.createElement('div');
            itemDiv.appendChild(nameDiv);
            nameDiv.innerText = "Наименование: " + catalogue.content[i].name;
            priceDiv = document.createElement('div');
            itemDiv.appendChild(priceDiv);
            priceDiv.innerText = "Цена: " + catalogue.content[i].price;
            // quantityDiv = document.createElement('div');
            // itemDiv.appendChild(quantityDiv);
            // quantityDiv.innerText = "Количество: " + catalogue.content[i].quantity;
            addButton = document.createElement('button');
            catalogueContainer.appendChild(addButton);
            addButton.innerText = "Добавить";
            addButton.onclick = basket.addItems;
            addButton.value = i;
        }

    }
}


