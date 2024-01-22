function one() {
    let val1 = Math.random() * 100;
    let val2 = Math.random() * 100;
    let result = val1 / val2;
    if (result % 1 === 0) {
        console.log(result);
    }
    if (result % 1 !== 0) {
        console.log(result.toFixed(2));
        document.getElementById('result1').innerText = "Division of two random numbers: " + result.toFixed(2);
    }
    // document.getElementById('result1').innerText = "Division of two random numbers: " + result;
}
one();

function two() {
    let str = "asdfghjklp";
    let with$ = str.split('').join('$');
    console.log("with$" + with$);
    let alp = str.split('').sort().join('');
    console.log("alphabetical_order  " + alp);
    document.getElementById('result2').innerText = "with '$' :" + with$ + ", Alphabetical_order: " + alp;
}
two();

function three() {
    let list = ["sugu", "vijay", "uva", "mani", "balaji"];
    let evenlist = [];
    let oddlist = [];
    for (let i = 0; i < list.length; i++) {
        if (i % 2 === 0) {
            evenlist.push(list[i]);
        }
        if (i % 2 !== 0) {
            oddlist.push(list[i]);
        }
    }
    console.log("Odd list " + oddlist);
    console.log("Even list " + evenlist);
    list = evenlist;
    document.getElementById('result3').innerText = "Evenlist from og list: " + list;
    list.splice(3, 0, "dhina", "hari");
    document.getElementById('result4').innerText = "After adding at 3rd position: " + list;
    list.sort();
    console.log("ascending order " + list);
    document.getElementById('result5').innerText = "Ascending order: " + list;
}
three();

function four() {
    list = [0, 9, 8, 7, 1, 2, 3, 4, 5, 6];
    list.sort();
    document.getElementById('result6').innerText = "Sorted list: " + list;
    let inclist = list.map(value => value + 1);
    console.log("incremeted list ", inclist);
    document.getElementById('result7').innerText = "Incremented list: " + inclist;
}
four();

function five() {
    let listdict = [
        { name: "sugumar", team: "product", selected: false },
        { name: "vijay", team: "product", selected: true },
        { name: "mani", team: "service", selected: false }
    ];
    for (let dictionary of listdict) {
        console.log(dictionary);
        document.getElementById('result8').innerText += "List of dictionary: " + JSON.stringify(dictionary) + "\n";
    }
    let selectedDictionary = listdict.find(dictionary => dictionary.selected === true);
    if (selectedDictionary) {
        for (let key in selectedDictionary) {
            console.log(key, selectedDictionary[key]);
            document.getElementById('result9').innerText += `Selected True: ${key} ${selectedDictionary[key]}\n`;
        }
    }
}

five();


function six(dictArray) {
    let list = [];
    for (let dict of dictArray) {
        if (list.length < 10) {
            list.push(dict);
        } else {
            document.getElementById('result10').innerText = "List is full";
            break;
        }
    }
    console.log("Dictionary added. Current list:", list);
    document.getElementById('result11').innerText = "Dictionary added. Current list: " + JSON.stringify(list);
}
six([
    { name: "sugu", age: 21, city: "chennai" },
    { name: "uva", age: 23, city: "bengaluru" },
    { name: "vijay", age: 26, city: "salem" },
    { name: "balaji", age: 24, city: "hosur" },
    { name: "john", age: 30, city: "new york" },
    { name: "alice", age: 28, city: "san francisco" },
    { name: "bob", age: 35, city: "los angeles" },
    { name: "emma", age: 25, city: "london" },
    { name: "alex", age: 27, city: "berlin" },
    { name: "maria", age: 22, city: "paris" },
    { name: "alex", age: 27, city: "berlin" },
    { name: "maria", age: 22, city: "paris" }
]);

function seven() {
    class Calculator {
        constructor(a, b) {
            this.a = a;
            this.b = b;
        }
        addition() {
            const result = this.a + this.b;
            this.displayResult(result);
        }
        subtraction() {
            const result = this.a - this.b;
            this.displayResult(result);
        }
        multiplication() {
            const result = this.a * this.b;
            this.displayResult(result);
        }
        displayResult(result) {
            document.getElementById('result12').innerText = 'Result: ' + result;
        }
    }    
    function action(calculator) {
        document.getElementById('add').addEventListener('click', () => calculator.addition());
        document.getElementById('sub').addEventListener('click', () => calculator.subtraction());
        document.getElementById('mul').addEventListener('click', () => calculator.multiplication());
    }
    
    const calculator = new Calculator(10, 5);
    action(calculator);
    
}
seven();
// nn
