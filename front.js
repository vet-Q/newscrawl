window.onload = function(){

    const btn = document.querySelector('#crawler');
    const wantprintdata = document.querySelector('#data');
    const div = document.querySelector('.textTable');
    const notice = document.querySelector('.notice');
    
    const dataset = async function(howto='GET') {
        const opts = {
                method:`${howto}`,
                headers:{},
        }
        let rest = await fetch('/data',opts);
        let data = await rest.json()
        console.log('nice')
        return data
    };
    
    
    const listMaker = (arr) => {
        const numTh = document.createElement('th');
        const titleTh = document.createElement('th');
        numTh.innerHTML = `<h3> 연번 </h3>`
        titleTh.innerHTML = `<h3> 기사제목 </h3>`
        wantprintdata.appendChild(numTh);
        wantprintdata.appendChild(titleTh);
        arr.forEach((val,idx)=>{
            let {title, link} = val
            let tr = document.createElement('tr');
            let numbertd = document.createElement('td');
            let titletd = document.createElement('td');
            numbertd.innerText = `${idx}`
            titletd.innerHTML = `<a href=${link}>${title}</a>`
            tr.appendChild(numbertd);
            tr.appendChild(titletd);
            wantprintdata.appendChild(tr)
        })
    
    }
    
    btn.addEventListener('click',async(e)=>{
        const p1 = document.createElement('p');
        p1.innerHTML = '<h1> 크롤링 중입니다. 잠시만 기다려주세요';
        notice.appendChild(p1);
        const wantprint = await dataset();
        notice.removeChild(p1);
        await listMaker(wantprint)
        const p = document.createElement('p');
        p.innerHTML = '<h1>데이터 작성이 완료되었습니다</h1>'
        setTimeout(()=>{notice.appendChild(p)},2000)

    });
};
    
    