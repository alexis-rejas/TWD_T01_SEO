// JavaScript principal - Optimización SEO de Páginas Web

// Navegación entre secciones
document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        const section = this.getAttribute('data-section');
        
        // Remover clase active de todos
        document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
        
        // Agregar clase active a los seleccionados
        this.classList.add('active');
        document.getElementById(section).classList.add('active');
    });
});

// Analizador SEO
function analyzeForSEO() {
    const title = document.getElementById('title').value.trim();
    const description = document.getElementById('description').value.trim();
    const keywords = document.getElementById('keywords').value.trim();
    const contentLength = document.getElementById('content-length').value;
    const mobileFriendly = document.getElementById('mobile-friendly').checked;
    const https = document.getElementById('https').checked;
    const fastLoad = document.getElementById('fast-load').checked;

    let score = 0;
    const issues = [];
    const successes = [];

    // Validar título
    if (title.length === 0) {
        issues.push("Falta el título de la página");
    } else if (title.length < 30) {
        issues.push("Título muy corto (menos de 30 caracteres)");
    } else if (title.length > 60) {
        issues.push("Título muy largo (más de 60 caracteres)");
    } else {
        score += 15;
        successes.push("Título optimizado correctamente");
    }

    // Validar descripción
    if (description.length === 0) {
        issues.push("Falta la meta descripción");
    } else if (description.length < 120) {
        issues.push("Descripción muy corta (menos de 120 caracteres)");
    } else if (description.length > 160) {
        issues.push("Descripción muy larga (más de 160 caracteres)");
    } else {
        score += 15;
        successes.push("Meta descripción optimizada");
    }

    // Validar palabras clave
    if (keywords.length === 0) {
        issues.push("No ingresaste palabras clave");
    } else if (keywords.split(',').length < 3) {
        issues.push("Deberías tener al menos 3 palabras clave principales");
    } else {
        score += 10;
        successes.push("Palabras clave definidas");
    }

    // Validar contenido
    if (contentLength === "yes") {
        score += 20;
        successes.push("Contenido suficiente (>300 palabras)");
    } else if (contentLength === "no") {
        issues.push("Contenido muy corto (menos de 300 palabras)");
    } else {
        issues.push("No indicaste la extensión del contenido");
    }

    // Validar responsive
    if (mobileFriendly) {
        score += 15;
        successes.push("Sitio adaptado para móvil");
    } else {
        issues.push("Sitio NO es responsive (penalización en Google)");
    }

    // Validar HTTPS
    if (https) {
        score += 15;
        successes.push("Sitio tiene HTTPS seguro");
    } else {
        issues.push("Sitio sin HTTPS (criterio de ranking importante)");
    }

    // Validar velocidad
    if (fastLoad) {
        score += 10;
        successes.push("Velocidad de carga optimizada");
    } else {
        issues.push("Sitio lento (afecta ranking y usuarios abandonan)");
    }

    // Mostrar resultado
    const resultDiv = document.getElementById('seo-result');
    const contentDiv = document.getElementById('result-content');

    let scoreClass = score >= 70 ? 'good' : score >= 40 ? 'medium' : 'bad';
    let scoreLabel = score >= 70 ? '¡Excelente!' : score >= 40 ? 'Necesita mejoras' : 'Muy deficiente';

    let html = `
        <div class="score ${scoreClass}">${score}/100 - ${scoreLabel}</div>
        
        <h4 style="color: #4caf50; margin-top: 20px;">✓ Lo que está bien:</h4>
        <ul class="checklist">
    `;

    successes.forEach(success => {
        html += `<li class="ok">${success}</li>`;
    });

    html += `</ul><h4 style="color: #f44336; margin-top: 20px;">✗ Problemas encontrados:</h4><ul class="checklist">`;

    issues.forEach(issue => {
        html += `<li class="fail">${issue}</li>`;
    });

    html += `</ul>`;

    if (score >= 70) {
        html += `<div class="card" style="background: #c8e6c9; border-color: #4caf50; margin-top: 20px;">
            <strong style="color: #2e7d32;">🎉 ¡Tu página está bien optimizada para SEO!</strong>
            <p style="margin-top: 10px; color: #2e7d32;">Ahora enfócate en crear contenido de calidad y obtener enlaces externos.</p>
        </div>`;
    } else if (score >= 40) {
        html += `<div class="card" style="background: #fff3cd; border-color: #ff9800; margin-top: 20px;">
            <strong style="color: #856404;">⚠️ Tu página necesita mejoras significativas</strong>
            <p style="margin-top: 10px; color: #856404;">Trabaja en los puntos rojos arriba para mejorar tu ranking en Google.</p>
        </div>`;
    } else {
        html += `<div class="card" style="background: #ffcdd2; border-color: #f44336; margin-top: 20px;">
            <strong style="color: #c62828;">❌ Tu página no está optimizada para SEO</strong>
            <p style="margin-top: 10px; color: #c62828;">Es probable que no aparezca en los resultados de Google. Implementa urgentemente las mejoras sugeridas.</p>
        </div>`;
    }

    contentDiv.innerHTML = html;
    resultDiv.classList.add('show');
}

// Permitir Enter para analizar
if (document.getElementById('keywords')) {
    document.getElementById('keywords').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') analyzeForSEO();
    });
}
