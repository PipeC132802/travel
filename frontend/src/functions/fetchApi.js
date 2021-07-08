export function fetchApi(endpoint, conf) {
    return fetch(endpoint, conf)
    .then((resp) => {
        if(resp.status >= 400) throw Error
        return resp.json()
    })
}