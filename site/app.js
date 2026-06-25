const links = window.SITE_LINKS || {};

document.getElementById("guide-link").href = links.guide || "guide.html";
document.getElementById("savings-link").href = links.savings || "#";
document.getElementById("budget-link").href = links.budget || "#";
document.getElementById("card-link").href = links.card || "#";

document.getElementById("email-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const msg = document.getElementById("form-msg");
  const endpoint = links.formEndpoint;

  if (!endpoint) {
    msg.textContent = "Email capture not configured yet.";
    return;
  }

  try {
    const res = await fetch(endpoint, {
      method: "POST",
      headers: { Accept: "application/json" },
      body: new FormData(e.target),
    });
    if (res.ok) {
      msg.textContent = "You are in. Check your inbox.";
      e.target.reset();
    } else {
      msg.textContent = "Something failed. Try again.";
    }
  } catch {
    msg.textContent = "Network error. Try again.";
  }
});
