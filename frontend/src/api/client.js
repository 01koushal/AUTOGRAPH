const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:5000/api";

async function request(path, params) {
  const url = new URL(`${BASE_URL}${path}`);
  if (params) {
    Object.entries(params).forEach(([key, value]) => {
      if (value !== undefined && value !== null && value !== "") {
        url.searchParams.set(key, value);
      }
    });
  }
  const res = await fetch(url);
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.error || `Request failed: ${res.status}`);
  }
  return res.json();
}

export const api = {
  cars: {
    list: () => request("/cars"),
    recent: () => request("/cars/recent"),
    get: (slug) => request(`/cars/${slug}`),
  },
  manufacturers: {
    list: () => request("/manufacturers"),
    popular: () => request("/manufacturers/popular"),
    get: (slug) => request(`/manufacturers/${slug}`),
  },
  upgrades: {
    list: (category) => request("/upgrades", { category }),
    categories: () => request("/upgrades/categories"),
  },
  search: (q) => request("/search", { q }),
};
