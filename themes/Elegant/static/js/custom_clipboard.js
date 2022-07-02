// copy code to clipboard

const highlights = document.querySelectorAll("div.highlight");
highlights.forEach(div => {
const copyButton = document.createElement("button");
copyButton.innerHTML = "Copy to clipboard";
copyButton.addEventListener("click", handleCopyButtonClick);
div.prepend(copyButton);
});

const copyToClipboard = str => {
const el = document.createElement("textarea"); // create a <textarea> element
el.value = str; // set its value to the string that you want copied
el.setAttribute("readonly", ""); // make it readonly to be tamper-proof
el.style.position = "absolute";
el.style.left = "-9999px"; // move outside the screen to make it invisible
// el.style.display = "none";
document.body.appendChild(el); // append the <textarea> element to the HTML document
const selected = document.getSelection().rangeCount > 0 // check if there is any content selected previously
? document.getSelection().getRangeAt(0) // store selection if found
: false; // mark as false to know no selection existed before
el.select(); // select the <textarea> content
document.execCommand("copy"); // copy - only works as a result of a user action (e.g. click events)
document.body.removeChild(el); // remove the <textarea> element
if(selected) {
document.getSelection().removeAllRanges(); // unselect everything on the HTML document
document.getSelection().addRange(selected); // restore the original selection
}
}

function handleCopyButtonClick(evt) {
const { children } = evt.target.parentElement;
const { innerText } = Array.from(children).at(-1);
copyToClipboard(innerText);
// alert(innerText);
}


function handleQuestion(e) {
document.write(e.parendNode());
}
