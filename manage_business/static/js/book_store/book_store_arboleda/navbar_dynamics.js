// define the arrays for the customer and staff links
const customerLinks = [
    { label: "Home", url: "/customer/home" },
    { label: "Cart", url: "/customer/cart" },
    { label: "Login", url: "/customer/login" },
    { label: "Logout", url: "/customer/logout" },
  ];
  
  const staffLinks = [
    { label: "Home", url: "/staff/home" },
    { label: "Add Book", url: "/staff/add-book" },
    { label: "Login", url: "/staff/login" },
    { label: "Logout", url: "/staff/logout" },
  ];
  
  // get the navbar element
  const navbar = document.querySelector("#navbar");
  
  // determine the user type (e.g. "customer" or "staff")
  const userType = "staff";
  
  // set the links array based on the user type
  const links = (userType === "customer") ? customerLinks : staffLinks;
  
  // loop through the links and create the navbar elements
  links.forEach(link => {
    const navbarLink = document.createElement("a");
    navbarLink.textContent = link.label;
    navbarLink.href = link.url;
    navbar.appendChild(navbarLink);
  });
  