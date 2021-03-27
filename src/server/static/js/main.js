
async function postData(url = '', data = {}) {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    return response.json();
  }

const appStart = () => {
    const dauButton = document.querySelector('#authenticate')
    dauButton.addEventListener('mousedown', (e) => {
      postData('/authenticate').then((x) => console.log(x))
    })
}

document.addEventListener('DOMContentLoaded', appStart);