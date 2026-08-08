function detectIntrusion() {

    const packet_count =
        document.getElementById("packet_count").value;

    const failed_logins =
        document.getElementById("failed_logins").value;

    const port =
        document.getElementById("port").value;

    fetch("/detect", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            packet_count: packet_count,
            failed_logins: failed_logins,
            port: port
        })
    })
    .then(response => response.json())
    .then(data => {

        document.getElementById("result").innerHTML =
            data.status + "<br>" + data.message;

    });
}