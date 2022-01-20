let XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;
let API = 'https://rickandmortyapi.com/api/character/';

const fetchData = (url_api) => {
    return new Promise((resolve, reject) => {
        const xhttp = new XMLHttpRequest();
        xhttp.open('GET', url_api, true);
        xhttp.onreadystatechange = (() => {
        if(xhttp.readyState === 4){
            (xhttp.status === 200)
            ? resolve(JSON.parse(xhttp.responseText))
            : reject(new Error('Error ' + url_api));
        }
    });
    xhttp.send();
});
}

module.export = fetchData;

/* fetchData(API, (error1, data1) => {
    if(error1) return console.error(error1);
    fetchData(API + data1.results[0].id, (error2, data2) =>{
        if(error2) return console.error(error2);
        fetchData(data2.origin.url, (error3, data3) =>{
            if(error3) return console.error(error3)
            console.log(data1.info.count);
            console.log(data2.name);
            console.log(data3.dimension);
        })
    })
}) */