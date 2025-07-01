import { JsonController, Get, Post, Put, Delete, Param, QueryParam, Body } from "routing-controllers";

@JsonController("/api/users")
export class UserController {
    private users: { id: number; name: string }[] = [];

    @Get("/")
    getAllUsers() {
        console.log("Fetching all users");
        return this.users;
    }

    @Get("/search")
    getUserByName(@QueryParam("name") name: string) {
        console.log(`Searching for user with name: ${name}`);
        const user = this.users.find(u => u.name.toLowerCase() === name.toLowerCase());
        if (!user) throw new Error("User not found");
        return user;
    }

    @Get("/:id")
    getUser(@Param("id") id: number) {
        console.log(`Fetching user with id: ${id}`);
        const user = this.users.find(u => u.id === id);
        if (!user) throw new Error("User not found");
        return user;
    }

    @Post("/")
    createUser(@Body() user: { name: string }) {
        console.log("Creating a new user:", user);
        const newUser = { id: this.users.length + 1, ...user };
        this.users.push(newUser);
        return newUser;
    }

    @Put("/:id")
    updateUser(@Param("id") id: number, @Body() user: { name: string }) {
        console.log(`Updating user with id: ${id}`, user);
        const index = this.users.findIndex(u => u.id === id);
        if (index === -1) throw new Error("User not found");
        this.users[index] = { id, ...user };
        return this.users[index];
    }

    @Delete("/:id")
    deleteUser(@Param("id") id: number) {
        console.log(`Deleting user with id: ${id}`);
        const index = this.users.findIndex(u => u.id === id);
        if (index === -1) throw new Error("User not found");
        const deletedUser = this.users.splice(index, 1);
        return deletedUser[0];
    }
}