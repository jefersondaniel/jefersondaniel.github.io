Title: Diminuindo o tempo de carregamento de sites
Slug: diminuindo-o-tempo-de-carregamento-de-sites
Date: 2015-06-29
Category: Dicas, Links

Com a popularidade de frameworks como AngularJS e a facilidade de plugins JQuery se tornou comum exagerar em quantidade de scripts e css. Também surgiram novos problemas de performance como a otimização para mobile e a performance do código javascript. Ainda assim os problemas graves de performance costumam ser os mesmos: Falta de cache e excesso de plugins.

Otimizar esses aspectos é algo que melhora tanto a usabilidade quanto a reputação no Google. Deixarei aqui coisas que levo em consideração e links relacionados.

* **Cache**: Melhora muito usar alguma solução de cache como o Varnish Cache pois o cache vai desafogar o servidor web da tarefa de servir tanto arquivos estáticos (imagens, scripts, css) quanto arquivos dinâmicos. Outra solução de cache que tenho usado para projetos pessoais é o serviço CloudFlare. A vantagem de usar um serviço assim é que, ao invés de configurar seu próprio Varnish, os arquivos estáticos são servidos diretamente do CloudFare. Ou seja,não consome servidores e tem um plano gratuito.

* **Unificação de arquivos javascript e css**: Juntar todos javascripts em um só e fazer o mesmo com os css pode diminuir o tempo de carregamento. Além disso, mover as tags de script para o fim do HTML também ajuda. Ferramentas como YSlow e Google Page Speed podem indicar a melhor forma de fazer essas e outras otimizações.

* **Carregamento preguiçoso (Lazy Loading)**: Suponha que você está fazendo uma site que consulta uma lista de produtos recomendados na página inicial. Se esse conteúdo for carregado junto com o restante do site o usuário terá de esperar tanto ele quanto as recomendações para ver tudo. Em casos assim é conveniente carregar somente o conteúdo do site e chamar o mais demorado em algum ajax, pois assim o usuário espera menos para ver o conteúdo principal.

Enfim, existe bastante coisa para se otimizar tempo de resposta e a solução  é estar continuamente usando ferramentas de teste. Eu uso YSlow para testes do frontend e Apache Benchmark (AB) para testes de carga no backend. Boa sorte com seus testes.

## Referências

* <a href="https://www.varnish-cache.org/" target="_blank">Vanish Cache</a>
* <a href="https://www.wptotal.com/duvidas-cloudflare/" target="_blank">Dúvidas sobre o Cloudfare</a>
* <a href="http://yslow.org/" target="_blank">YSlow</a>
