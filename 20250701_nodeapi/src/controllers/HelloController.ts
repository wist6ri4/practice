import { JsonController, Get, Post, Body } from "routing-controllers";

@JsonController("/api")
export class HelloController {
    @Get("/hello")
    getHello(): string {
        console.log("Hello endpoint was called");
        return "Hello, World!";
    }

    @Post("/echo")
    postEcho(@Body() body: any) {
        console.log("Echo endpoint was called with body:", body);
        return {
            message: "Echoing back your data",
            data: body
        };
    }
}