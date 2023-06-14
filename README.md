[![YT](https://i.ytimg.com/vi/Vf63ou4VyOQ/maxresdefault.jpg)](https://www.youtube.com/watch?v=Vf63ou4VyOQ)
[https://www.youtube.com/watch?v=Vf63ou4VyOQ]()


No vídeo de hoje, vou mostrar como acelerar o desempenho do Python usando a biblioteca Numba. Vamos explorar duas abordagens: compilação Just-in-Time (JIT) e compilação Ahead-of-Time (AOT).

Numba é uma biblioteca poderosa que permite otimizar o desempenho de códigos em Python, especialmente quando trabalhamos com cálculos numéricos intensivos. Ela utiliza técnicas de compilação just-in-time para gerar código de máquina altamente otimizado, o que resulta em uma execução significativamente mais rápida.

No primeiro exemplo, usaremos a compilação JIT para acelerar a busca de coordenadas em uma imagem utilizando a biblioteca PIL e o Numba. Mostrarei como podemos encontrar as coordenadas de todos os pixels que correspondem a uma determinada cor. Com o Numba, podemos utilizar a diretiva @njit(parallel=True) para paralelizar o código, aproveitando ao máximo o poder dos processadores modernos. Demonstrarei como essa abordagem pode ser aplicada tanto para encontrar coordenadas de um único pixel, quanto para encontrar coordenadas de várias cores simultaneamente.

Em seguida, vamos dar um passo além e explorar a compilação Ahead-of-Time (AOT) com o Numba. Utilizaremos a biblioteca numba-aot-compiler para compilar o código em tempo de compilação. Mostrarei como podemos acelerar a busca de cores em uma imagem utilizando a técnica AOT. Com isso, obteremos ganhos adicionais de desempenho, pois o código já estará compilado quando executarmos o programa.

Além de acelerar a execução do Python, o uso do Numba traz outras vantagens. Ele simplifica o processo de otimização de código, permitindo que os desenvolvedores escrevam código Python puro e ainda assim obtenham um desempenho comparável ao de linguagens de programação de baixo nível, como C e C++. Isso significa que podemos obter velocidade sem sacrificar a produtividade e a facilidade de desenvolvimento proporcionadas pelo Python.

Ao final do vídeo, você terá aprendido como usar o Numba para acelerar o seu código Python, seja com a compilação Just-in-Time (JIT) ou com a compilação Ahead-of-Time (AOT). Você verá como é possível melhorar significativamente o desempenho de suas aplicações, especialmente aquelas que envolvem cálculos numéricos intensivos.

Então, não perca mais tempo! Assista ao vídeo e comece a aproveitar os benefícios do Numba para acelerar os seus projetos em Python. Tenho certeza de que você ficará impressionado com os resultados.

Se gostou do vídeo, não se esqueça de deixar o seu like, compartilhar com seus amigos e se inscrever no canal para acompanhar mais conteúdos como esse. Aproveite!

Código usado no vídeo: https://github.com/hansalemaos/tutorial_acelerando_python_com_numba

### Projetos nos quais usei Numba

https://github.com/hansalemaos/locate_pixelcolor_numba
https://github.com/hansalemaos/numba_aot_compiler
https://github.com/hansalemaos/locate_pixelcolor_numbacuda
https://github.com/hansalemaos/charchef
