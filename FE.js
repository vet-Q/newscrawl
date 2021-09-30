window.onload = function(){

const btn = document.querySelector('#crawler');
const wantprintdata = document.querySelector('#data');
const form = document.querySelector('.disease');

const dataset = async function(howto='GET') {
    const opts = {
            method:`${howto}`,
            headers:{},
    }
    let res = await fetch('/data',opts);
    let data = await res.json();
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
    const wantprint = await dataset();
    let arr = wantprint['African swine fever'];
    listMaker(arr);
});

// form.addEventListener('submit',async function(e){
//     e.preventDefault;
//     console.log(this)

//     console.log('hello world')
//     // const wantprint = await dataset("POST");
//     // let disease = wantprint.keys[0];
//     // let arr = wantprint[disease];

};

