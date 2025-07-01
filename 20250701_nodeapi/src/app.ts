import "reflect-metadata";
import { createExpressServer } from "routing-controllers";
import { HelloController } from "./controllers/HelloController";
import { UserController } from "./controllers/UserController";

const app = createExpressServer({
    controllers: [HelloController, UserController],
});

app.listen(3000, () => {
    console.log("Server is running on http://localhost:3000");
})