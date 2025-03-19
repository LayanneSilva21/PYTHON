alert('Boas vindas ao jogo do número secreto');
let numeroMaximo = 5000;
let numeroSecreto = parseInt(Math.random() * numeroMaximo + 1);
console.log(numeroSecreto);
let chute;
let tentativas = 1;

while (chute != numeroSecreto) {
    chute = prompt(`Escolha um numero entre 1 e ${numeroMaximo}`);
if(chute == numeroSecreto){
    alert(`Voce acertou o numero secreto com ${tentativas} tentativas`);
} else {
    if (chute > numeroSecreto) {
            alert(`O número secreto é menor que ${chute}`);
    } else {
            alert(`O número secreto é maior que ${chute}`);
    }
}
tentativas++;
}
let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';
alert(`O número secreto era ${numeroSecreto} e você acertou com apenas ${tentativas} ${palavraTentativa}`);