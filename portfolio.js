'use strict';
for(const button of document.querySelectorAll('[data-filter]'))button.addEventListener('click',()=>{
 const filter=button.dataset.filter;
 for(const b of document.querySelectorAll('[data-filter]')){const selected=b===button;b.classList.toggle('selected',selected);b.setAttribute('aria-pressed',String(selected));}
 for(const entry of document.querySelectorAll('[data-app]'))entry.hidden=filter!=='all'&&entry.dataset.app!==filter;
});
