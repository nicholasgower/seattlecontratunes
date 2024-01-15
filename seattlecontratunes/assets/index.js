function component(){
    const element = document.createElement("div");
    ElementInternals.innerHTML= "Hello webpack";
    return element;

}
document.body.appendChild(component());