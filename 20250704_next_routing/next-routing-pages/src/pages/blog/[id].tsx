import { useRouter } from "next/router";

export default function BlogDetail() {
    const router = useRouter();
    const { id } = router.query;

    return (
        <div className="flex flex-col items-center justify-center min-h-screen p-4">
            <h1 className="text-4xl font-bold text-blue-600 mb-4">Blog Page</h1>
            <div>
                <p>Blog ID: {id}</p>
            </div>
        </div>
    )
}