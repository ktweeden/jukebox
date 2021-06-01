
async function getData(url = '') {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      },
    });
    return response.json();
  }

const appStart = () => {
    const authenticateButton = document.querySelector('#authenticate')
    authenticateButton.addEventListener('mousedown', (e) => {
      getData('/authenticate').then((x) => console.log(x))
    })
}

document.addEventListener('DOMContentLoaded', appStart);