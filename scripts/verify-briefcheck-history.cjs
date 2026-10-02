const fs=require('node:fs'),path=require('node:path'),{execFileSync}=require('node:child_process');
const root=path.resolve(__dirname,'..'),dir=path.join(root,'.work','briefcheck-history');
fs.mkdirSync(path.dirname(dir),{recursive:true});
if(!fs.existsSync(path.join(dir,'.git')))execFileSync('git',['clone',path.join(root,'evidence','briefcheck-history.bundle'),dir],{stdio:'inherit'});
const cases=[['V1','f0c13dca045272df7d696a6d48aa0bc0ea5ce35d',6],['V2','7a51bf1128903aec7ceec35aa23077437d1ce9b7',12],['V3','10fd0e8f171c963fb46f719be65d8ecb7f9beb93',12]];
for(const [version,ref,expected] of cases){const result=execFileSync(process.execPath,[path.join(dir,'tests','benchmark.cjs'),ref],{cwd:dir,encoding:'utf8'});const data=JSON.parse(result.trim().split(/\r?\n/).at(-1));console.log(version,JSON.stringify(data));if(data.passed!==expected||data.total!==12)process.exitCode=1;}
