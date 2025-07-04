import Link from "next/link";

export default function Home() {
    return (
        <div className="flex flex-col items-center justify-center min-h-screen p-4">
            <h1>Home Page</h1>
            <p>This is a link page.</p>
            <div className="border border-gray-300 border- rounded-lg p-4 mt-4 shadow-md shadow-gray-500 columns-2">
                <div>
                    <Link href="/" className="text-blue-100 underline">Go to Index</Link>
                </div>
                <div>
                    <Link href="/about" className="text-blue-400 underline">Go to About</Link>
                </div>
                <div>
                    <Link href="/blog/20" className="text-blue-700 underline">Go to Blog 20</Link>
                </div>
            </div>
        </div>
    );
}