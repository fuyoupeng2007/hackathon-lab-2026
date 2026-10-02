const http=require('node:http'),fs=require('node:fs'),path=require('node:path');
const root=__dirname;
http.createServer((req,res)=>{
 let pathname;try{pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname);}catch{res.writeHead(400).end();return;}
 const file=path.resolve(root,'.'+pathname+(pathname.endsWith('/')?'index.html':''));
 if(!file.startsWith(root+path.sep)||pathname.split('/').some(x=>x.startsWith('.')||['qa','delivery','scripts','evidence'].includes(x))){res.writeHead(404).end();return;}
 const types={'.html':'text/html','.css':'text/css','.js':'text/javascript','.json':'application/json','.md':'text/markdown','.pdf':'application/pdf','.png':'image/png','.mp4':'video/mp4','.srt':'text/plain'};
 fs.readFile(file,(err,data)=>{if(err){res.writeHead(404).end('Not found');return;}res.writeHead(200,{'Content-Type':(types[path.extname(file)]||'application/octet-stream')+'; charset=utf-8','X-Content-Type-Options':'nosniff','Cache-Control':'no-store'});res.end(data);});
}).listen(Number(process.env.PORT||4399),'127.0.0.1',()=>console.log('Hackathon Lab: http://127.0.0.1:4399'));
