// function searchView() {
//   var self = this;
//   self.fName = ko.observable("tanvir");
// }

// ko.applyBindings(new searchView(), document.querySelector(".search"));

const navLink = document.getElementsByClassName("nav-container");
const icon = document.querySelectorAll("#Icon");
for (let i = 0; i < navLink.length; i++) {
  navLink[i].addEventListener("click", function () {
    var y = i - 3;
    this.classList.toggle("active");
    if (icon[y].classList.contains("fa-angle-down")) {
      icon[y].classList.replace("fa-angle-down", "fa-angle-up");
    } else {
      icon[y].classList.replace("fa-angle-up", "fa-angle-down");
    }
  });
}
