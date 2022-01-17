// const loginInput = document.getElementById('login-email');
// loginInput.focus();

let coll = document.getElementsByClassName('collapsible');
let i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener('click', function () {
        this.classList.toggle('active');
        var content = this.nextElementSibling;
        if (content.style.display === 'block') {
            content.style.display = 'none';
            console.log('if');
        } else {
            content.style.display = 'block';
            console.log('else');
        }
    });
}
