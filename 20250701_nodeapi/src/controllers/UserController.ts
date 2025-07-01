import { JsonController, Get, Post, Put, Delete, Param, QueryParam, Body } from "routing-controllers";

/**
 * UserController
 * ユーザー管理のためのコントローラーサンプル
 * - ユーザーの取得、作成、更新、削除を行う
 */
@JsonController("/api/users")
export class UserController {
    private users: { id: number; name: string }[] = [];

    /**
     * 全ユーザーを取得する
     * @returns ユーザーのリスト
     */
    @Get("/")
    getAllUsers() {
        console.log("Fetching all users");
        return this.users;
    }

    /**
     * 名前でユーザーを検索する
     * @param name 検索するユーザーの名前
     * @return ユーザー情報
     * @throws ユーザーが見つからない場合はエラーをスロー
     */
    @Get("/search")
    getUserByName(@QueryParam("name") name: string) {
        console.log(`Searching for user with name: ${name}`);
        const user = this.users.find(u => u.name.toLowerCase() === name.toLowerCase());
        if (!user) throw new Error("User not found");
        return user;
    }

    /**
     * 特定のIDのユーザーを取得する
     * @param id ユーザーのID
     * @return ユーザー情報
     * @throws ユーザーが見つからない場合はエラーをス
     */
    @Get("/:id")
    getUser(@Param("id") id: number) {
        console.log(`Fetching user with id: ${id}`);
        const user = this.users.find(u => u.id === id);
        if (!user) throw new Error("User not found");
        return user;
    }

    /**
     * 新しいユーザーを作成する
     * @param user 作成するユーザーの情報
     * @return 作成されたユーザー情報
     * @throws ユーザーの作成に失敗した場合はエラーをスロー
     */
    @Post("/")
    createUser(@Body() user: { name: string }) {
        console.log("Creating a new user:", user);
        const newUser = { id: this.users.length + 1, ...user };
        this.users.push(newUser);
        return newUser;
    }

    /**
     * 特定のIDのユーザーを更新する
     * @param id 更新するユーザーのID
     * @param user 更新するユーザーの情報
     * @return 更新されたユーザー情報
     * @throws ユーザーが見つからない場合はエラーをスロー
     */
    @Put("/:id")
    updateUser(@Param("id") id: number, @Body() user: { name: string }) {
        console.log(`Updating user with id: ${id}`, user);
        const index = this.users.findIndex(u => u.id === id);
        if (index === -1) throw new Error("User not found");
        this.users[index] = { id, ...user };
        return this.users[index];
    }

    /**
     * 特定のIDのユーザーを削除する
     * @param id 削除するユーザーのID
     * @return 削除されたユーザー情報
     * @throws ユーザーが見つからない場合はエラーをスロー
     */
    @Delete("/:id")
    deleteUser(@Param("id") id: number) {
        console.log(`Deleting user with id: ${id}`);
        const index = this.users.findIndex(u => u.id === id);
        if (index === -1) throw new Error("User not found");
        const deletedUser = this.users.splice(index, 1);
        return deletedUser[0];
    }
}