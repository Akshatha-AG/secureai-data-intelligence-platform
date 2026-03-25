async function uploadFile() {
    console.log("Button clicked");

    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    displayResult(data);
}

function displayResult(data) {
    let html = "";

    html += `<h3>Summary:</h3><p>${data.summary}</p>`;
    html += `<h3>Risk Score:</h3><p>${data.risk_score}</p>`;
    html += `<h3>Risk Level:</h3><p>${data.risk_level}</p>`;

    html += `<h3>Insights:</h3><ul>`;
    data.insights.forEach(i => {
        html += `<li>${i}</li>`;
    });
    html += `</ul>`;

    html += `<h3>Findings:</h3><ul>`;
    data.findings.forEach(f => {
        html += `<li>[${f.type}] Line ${f.line} → ${f.content}</li>`;
    });
    html += `</ul>`;

    document.getElementById("result").innerHTML = html;
}