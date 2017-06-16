# APICalculadora
API para realização de cálculos matemáticos, com base em uma requisição POST com a propriedade expressão recebendo o calculo a se fazer.

Exemplo de uso:</br>

POST JSON: http://seuendereco:8080/calcule</br>
Header: application/json
</br>
Body:
</br>
{</br>
  "expressao": "(5-2)+4*10/(45+2)"</br>
}

</br></br>Retorno:</br></br>
{</br>
    "expressao": </br>{</br>
        "expressao": "(5-2)+4*10/(45+2)"</br>
				},</br>
    "resultado": 3.851063829787234</br>
}
  
