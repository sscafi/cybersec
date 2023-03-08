// Register the service worker
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js');
  }
  
  // Intercept fetch requests and return cached responses
  self.addEventListener('fetch', function(event) {
    // Ignore requests that are not GET requests
    if (event.request.method !== 'GET') {
      return;
    }
  
    // Ignore requests that are for resources that are not needed
    if (event.request.url.includes('unnecessary-resource')) {
      return;
    }
  
    // Respond with a cached response if available
    event.respondWith(
      caches.match(event.request).then(function(cachedResponse) {
        if (cachedResponse) {
          return cachedResponse;
        }
  
        // Otherwise, fetch the request from the network and cache it
        return fetch(event.request).then(function(networkResponse) {
          caches.open('my-cache').then(function(cache) {
            cache.put(event.request, networkResponse.clone());
          });
  
          return networkResponse;
        });
      })
    );
  });
  