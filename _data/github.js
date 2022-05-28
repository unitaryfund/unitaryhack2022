// const fetch = require("node-fetch");
// const flatcache = require("flat-cache");
// const path = require("path");

// function getDateKey() {
//     let date = new Date();
//     return `${date.getUTCFullYear()}-${date.getUTCMonth() + 1}-${date.getUTCDate()}`;
// }

// module.exports = async function() {
//     let cache = flatcache.load("github-scrape", path.resolve("./_datacache"));
//     let key = getDateKey();
//     let cachedData = cache.getKey(key);
//     if (!cachedData) {
//         console.log("Fetching new github stats…");
//         //https://developer.github.com/v3/repos/#get
//         let newData = await fetch("https://api.github.com/repos/unitaryfund/mitiq", { method: 'GET', headers: { 'Content-Type': 'application/json' } })
//             .then(res => res.json())
//             .then(json => {
//                 //return json
//                 return {
//                     name: json.name,
//                     full_name: json.full_name,
//                     html_url: json.html_url,
//                     description: json.description,
//                     url: json.url,
//                     created_at: json.created_at,
//                     updated_at: json.updated_at,
//                     clone_url: json.clone_url,
//                     homepage: json.homepage,
//                     size: json.size,
//                     stargazers_count: json.stargazers_count,
//                     watchers_count: json.watchers_count,
//                     language: json.language,
//                     forks_count: json.fork_count,
//                     license: {
//                         key: json.license.key,
//                         name: json.license.name,
//                         spdx_id: json.license.spdx_id,
//                         url: json.license.url
//                     },
//                     topics: json.topics,
//                     open_issues: json.open_issues
//                 };
//             });
//         console.log(key)
//         console.log(newData)
//         cache.setKey(key, newData);
//         cache.save();

//         return newData;
//     }

//     return cachedData;
// };