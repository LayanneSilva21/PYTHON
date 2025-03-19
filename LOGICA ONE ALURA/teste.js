alert('Boas vindas ao novo jogo!');
let nome = prompt('Qual o seu nome? ');
alert('Olá ' + nome + ' Seja bem-vindo!');
console.log('Olá ' + nome + ' Seja bem-vindo!');

let resp = prompt('Qual sua linguagem de programação você mais gosta?');

alert(`${nome} sua linguagem de programação favorita é ${resp}`);
console.log(`${nome} sua linguagem de programação favorita é ${resp}`);


let valor1 = prompt('Digite um numero:');

let valor2 = prompt('Digite o outro numero: ');

let result = parseInt(valor1) + parseInt(valor2); 

alert(`A soma entre ${valor1} e ${valor2} é ${result}`);
console.log(`A soma entre ${valor1} e ${valor2} é ${result}`);

let idade = prompt('Qual a sua idade? ');

if(idade >= 18){
    alert('Maior de idade');
    console.log('Maior de idade');
}else{
    alert('Menor de idade');
    console.log('Menor de idade');
}

let numero = parseInt(prompt('Digite um número'));

if(numero > 0) {
    console.log('Positivo')
} 
else if(numero < 0) {
    console.log('Negativo')
}
else {
    console.log('Zero')
}

let inicial = 1;
let final = 10;

while(inicial <= final) {
    console.log(inicial)
    inicial++;
}

let nota1 = parseInt(prompt('Informe a primeira nota: '));

if(nota1>= 7){
    alert('Aprovado!')
    console.log('Aprovado!')
}else{
    alert('Reprovado!')
    console.log('Reprovado!')
}

let numAleatorio = Math.random()
console.log(numAleatorio)

let numAleatorio1 = parseInt(Math.random() * 10 + 1)
console.log(numAleatorio1)

let numAleatorio2 = parseInt(Math.random() * 1000 + 1)
console.log(numAleatorio2)

