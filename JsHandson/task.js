console.log("hello");

function numbertype() {
    let numInput = document.getElementById("numberInput").value;
    let num = parseFloat(numInput);
    let formattedNum = num.toFixed(2);
    document.getElementById("result1").innerText = "Formatted Number: " + formattedNum;
    document.getElementById("result2").innerText = "Precision: " + num.toPrecision(5);
    document.getElementById("result3").innerText = "To String: " + num.toString();
    document.getElementById("result4").innerText = "Is NaN: " + isNaN(num);
    document.getElementById("result5").innerText = "Round: " + Math.round(num);
    document.getElementById("result6").innerText = "Floor: " + Math.floor(num);
    document.getElementById("result7").innerText = "Ceil: " + Math.ceil(num);
    document.getElementById("result8").innerText = "Random Number: " + Math.random();
}
function stringtype() {
    let str = document.getElementById("Textinput").value.toString();
    document.getElementById("result9").innerText = "Length: " + str.length;
    document.getElementById("result10").innerText = "charAt: " + str.charAt(0);
    document.getElementById("result11").innerText = "concat: " + str.concat(" from salem");
    document.getElementById("result12").innerText = "indexOf is: " + str.lastIndexOf("is",3);
    document.getElementById("result13").innerText = "slice: " + str.slice(0,5);
    document.getElementById("result14").innerText = "toUpperCase: " + str.toUpperCase();
    document.getElementById("result15").innerText = "toLowerCase: " + str.toLowerCase();
    document.getElementById("result16").innerText = "replace: " + str.replace("sugumar", "vijay");
}
function array() {
    let arr = document.getElementById("inputarray").value;
    document.getElementById("result17").innerText ="Array :" + arr;
    let splitted = arr.split(',');
    let trimmed = splitted.map(element => element.trim())
    let a = trimmed;
    console.log("Input array is " + a);
    a.push("papaya");
    document.getElementById("result18").innerText = "push: " + a;
    let poppedElement = a.pop();
    document.getElementById("result19").innerText = "pop: " + a;
    a.unshift("tomato");
    document.getElementById("result20").innerText = "unshift: " + a;
    let shiftedElement = a.shift();
    document.getElementById("result21").innerText = "shift: " + a;
}
function loop(){
    for (let i = 0; i < 5; i++) {
        console.log(i);
    }
    
};
loop()
function map(){
    m=new Map();
    m.set("name","sugumar");
    m.set("team","product");
    console.log("Name",m.get("name"));
    console.log(m.has("age"));
    m.delete("team");
    console.log(m)
    console.log("map size",m.size);
    clearmap=m.clear();
    console.log(clearmap)

}
map()
function classobject(){
    class detail{
            constructor(name,age){
                this.name=name;
                this.age=age;
            }
    }
    person=new detail("sugumar",21);
    console.log(person.name);
}
classobject()
function assain_name(){
    let name="sugumar";
    return name;
}
function welcome(){
    console.log("Welcome "+ assain_name())
}
async function main(){
    console.log("first");
    const user_name= await assain_name();
    console.log(user_name);
    console.log("second")
    const welcomes = await welcome();
    console.log(welcomes);
}
main()