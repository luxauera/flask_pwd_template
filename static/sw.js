self.addEventListener('install', function (event) {
    console.log('[Service Worker] Installed');
    event.waitUntil(
        caches.open('todo-cache').then(function (cache) {
            return cache.addAll([
                '/',
                '/static/style.css',
                '/static/script.js',
                '/static/manifest.json'
            ]);
        })
    );
});

self.addEventListener('fetch', function (event) {
    event.respondWith(
        caches.match(event.request).then(function (response) {
            return response || fetch(event.request);
        })
    );
});
