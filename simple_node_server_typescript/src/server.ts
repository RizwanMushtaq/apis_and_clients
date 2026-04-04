import http, { IncomingMessage, ServerResponse } from "http";

const server = http.createServer(
  (req: IncomingMessage, res: ServerResponse) => {
    const url = req.url || "/";

    if (url === "/") {
      res.end("Home page");
    } else if (url === "/about") {
      res.end("About page");
    } else if (url === "/api") {
      res.setHeader("Content-Type", "application/json");
      res.end(JSON.stringify({ message: "Hello API" }));
    } else {
      res.statusCode = 404;
      res.end("Not found");
    }
  },
);

server.listen(3000, () => {
  console.log("Server running on port 3000");
});
