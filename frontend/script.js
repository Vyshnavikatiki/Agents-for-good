async function askAgent() {
    const agent = document.getElementById("agent").value;
    const query = document.getElementById("query").value;

    const responseBox = document.getElementById("response");
    responseBox.innerHTML = "Loading...";

    const res = await fetch(`http://127.0.0.1:8001/${agent}/ask`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
    });

    const data = await res.json();
    responseBox.innerHTML = data.response || "No response";
}
