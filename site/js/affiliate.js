// Shared affiliate helpers — loaded after config.js
function affiliateUrl(base) {
  const cfg = window.MONEY_CONFIG || {};
  if (!base) return "#";
  if (cfg.amazonTag && base.includes("amazon.")) {
    const sep = base.includes("?") ? "&" : "?";
    return base + sep + "tag=" + cfg.amazonTag;
  }
  return base;
}

function renderAffiliateBox(containerId, key, title, desc, cta) {
  const el = document.getElementById(containerId);
  if (!el) return;
  const cfg = window.MONEY_CONFIG || {};
  const url = affiliateUrl(cfg.affiliates?.[key] || "#");
  el.innerHTML = `
    <h3>${title}</h3>
    <p>${desc}</p>
    <a class="btn" href="${url}" target="_blank" rel="noopener sponsored">${cta}</a>
  `;
}
