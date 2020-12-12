const e1packbundles = document.getElementById("E1pack");
const p1packbundles = document.getElementById("P1pack");
const f1packbundles = document.getElementById("F1pack");
const e2packbundles = document.getElementById("E2pack");
const p2packbundles = document.getElementById("P2pack");
const f2packbundles = document.getElementById("F2pack");
const e3packbundles = document.getElementById("E3pack");
const p3packbundles = document.getElementById("P3pack");
const f3packbundles = document.getElementById("F3pack");
const ocspackbundles = document.getElementById("OPCaseStudy");
const mcspackbundles = document.getElementById("MGCaseStudy");
const scspackbundles = document.getElementById("STCaseStudy");

if (localStorage.getItem("levels")== "E1cima"){
    e1packbundles.style.display = "block";
}
if (localStorage.getItem("levels")== "P1cima"){
    p1packbundles.style.display = "block";
}
if (localStorage.getItem("levels")== "F1cima"){
    f1packbundles.style.display = "block";
}
if (localStorage.getItem("levels")== "E2cima"){
    e2packbundles.style.display = "block";
}
if (localStorage.getItem("levels")== "P2cima"){
    p2packbundles.style.display = "block";
}
if (localStorage.getItem("levels")== "F2cima"){
    f2packbundles.style.display = "block";
}
if (localStorage.getItem("levels")== "E3cima"){
    e3packbundles.style.display = "block";
}
if (localStorage.getItem("levels")== "P3cima"){
    p3packbundles.style.display = "block";
}
if (localStorage.getItem("levels")== "F3cima"){
    f3packbundles.style.display = "block";
}
if (localStorage.getItem("levels")== "ocscima"){
    ocspackbundles.style.display = "block";
}
if (localStorage.getItem("levels")== "mcscima"){
    mcspackbundles.style.display = "block";
}
if (localStorage.getItem("levels")== "scscima"){
    scspackbundles.style.display = "block";
}