document.addEventListener('DOMContentLoaded', () => {
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const audioElement = document.getElementById('audio');
    const source = audioContext.createMediaElementSource(audioElement);
    const analyser = audioContext.createAnalyser();
    source.connect(analyser);
    analyser.connect(audioContext.destination);
    analyser.fftSize = 256;

    const canvas = document.getElementById('canvas');
    const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, 150);

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / 150, 0.1, 1000);
    camera.position.z = 100;

    // Gradient Background
    const backgroundTexture = new THREE.TextureLoader().load('https://via.placeholder.com/800x150/000000/FFFFFF?text='); // Placeholder for gradient background
    scene.background = backgroundTexture;

    // Lights
    const ambientLight = new THREE.AmbientLight(0x666666);
    scene.add(ambientLight);

    const pointLight1 = new THREE.PointLight(0xffffff, 2, 500);
    pointLight1.position.set(50, 50, 50);
    scene.add(pointLight1);

    const pointLight2 = new THREE.PointLight(0xffffff, 1.5, 500);
    pointLight2.position.set(-50, -50, -50);
    scene.add(pointLight2);

    const barCount = analyser.frequencyBinCount;
    const bars = [];

    function createBars() {
        const barWidth = 4;
        const spacing = 7;
        const marginLeft = 270;

        bars.forEach(bar => scene.remove(bar));
        bars.length = 0;

        for (let i = 0; i < barCount; i++) {
            const geometry = new THREE.CylinderGeometry(1, 1, 6, 32);
            const material = new THREE.MeshPhongMaterial({ color: 0x25a56a, shininess: 80 });
            const bar = new THREE.Mesh(geometry, material);

            bar.position.x = marginLeft + (i - barCount / 2) * (barWidth + spacing);
            bar.rotation.x = Math.PI / 4;
            bar.rotation.z = Math.PI / 4;

            // Animation effect
            bar.userData.rotationSpeed = Math.random() * 0.01;

            scene.add(bar);
            bars.push(bar);
        }
    }

    function resizeCanvas() {
        const width = window.innerWidth;
        const height = 150;
        canvas.width = width;
        canvas.height = height;
        renderer.setSize(width, height);
        camera.aspect = width / height;
        camera.updateProjectionMatrix();
    }

    window.addEventListener('resize', () => {
        resizeCanvas();
        createBars();
    });

    resizeCanvas();
    createBars();

    function animate() {
        requestAnimationFrame(animate);

        const dataArray = new Uint8Array(analyser.frequencyBinCount);
        analyser.getByteFrequencyData(dataArray);

        for (let i = 0; i < bars.length; i++) {
            bars[i].scale.y = dataArray[i] / 10;

            const color = new THREE.Color('#25a56a');
            const lightness = 0.5 + (dataArray[i] / 256) * 0.5;
            bars[i].material.color.set(color.clone().lerp(new THREE.Color('#1a8b50'), lightness));

            // Apply rotation for 3D effect
            bars[i].rotation.y += bars[i].userData.rotationSpeed;
        }

        renderer.render(scene, camera);
    }

    animate()
});