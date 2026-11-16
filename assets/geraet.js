/* Am Computer: Entwurf im Handy-Rahmen zeigen (assets/handy.html). Auf dem Handy bleibt alles normal. */
(function(){try{
 if(window.self!==window.top||/[?&]frame=1/.test(location.search)||window.innerWidth<760||/HeadlessChrome/.test(navigator.userAgent))return;
 var base=document.currentScript.src.replace(/geraet\.js.*$/,'');
 location.replace(base+'handy.html?u='+encodeURIComponent(location.pathname));
}catch(e){}})();
