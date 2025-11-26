const canvas = document.getElementById('orbitCanvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

function drawOrbit(radius, color, speed) {
  ctx.beginPath();
  ctx.strokeStyle = color;
  ctx.lineWidth = 1;
  ctx.arc(canvas.width/2, canvas.height/2, radius, 0, Math.PI * 2);
  ctx.stroke();

  const angle = Date.now() / speed;
  const x = canvas.width/2 + Math.cos(angle) * radius;
  const y = canvas.height/2 + Math.sin(angle) * radius;

  ctx.beginPath();
  ctx.fillStyle = '#00ffff';
  ctx.arc(x, y, 3, 0, Math.PI * 2);
  ctx.fill();
}

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (let i = 100; i <= 300; i += 40) {
    drawOrbit(i, '#0ff3', 2000 + i * 10);
  }
  requestAnimationFrame(animate);
}
animate();
