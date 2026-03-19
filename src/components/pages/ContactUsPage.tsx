import { Button } from "@/components/ui/button";
import { toast } from "sonner";
import { ArrowLeft, Mail, Globe, Github } from "lucide-react";

interface ContactUsPageProps {
  onBack: () => void;
}

export function ContactUsPage({ onBack }: ContactUsPageProps) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(235,245,255)] dark:from-gray-900 dark:to-gray-800">
      {/* Header */}
      <header className="bg-white dark:bg-gray-900 border-b border-[rgb(200,220,240)] dark:border-gray-700 shadow-sm">
        <div className="max-w-4xl mx-auto px-6 py-4 flex items-center justify-between">
          <button onClick={onBack} className="text-[rgb(50,135,200)] hover:text-[rgb(40,115,175)] transition-colors">
            <ArrowLeft className="w-6 h-6" />
          </button>
        </div>
      </header>

      {/* Content */}
      <main className="max-w-4xl mx-auto px-6 py-10">
        <div className="mb-8 text-center">
          <h2 className="text-2xl font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]">
            Get in Touch
          </h2>
          <p className="text-sm text-muted-foreground">
            Have questions or feedback? We'd love to hear from you.
          </p>
        </div>

        <div className="space-y-8 max-w-2xl mx-auto">
          {/* Contact Information */}
          <div className="p-6 bg-white dark:bg-gray-800 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md space-y-4">
              <h3 className="text-base font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">
                Contact Information
              </h3>
              <div className="space-y-2">
                <p className="text-sm flex items-center gap-2">
                  <Mail className="w-4 h-4 text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]" />
                  <span><span className="font-medium text-foreground">Email: </span><a href="mailto:sdx-support@renci.org" className="text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] hover:underline">sdx-support@renci.org</a></span>
                </p>
                <p className="text-sm flex items-center gap-2">
                  <Globe className="w-4 h-4 text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]" />
                  <span><span className="font-medium text-foreground">Website: </span><a href="https://www.atlanticwave-sdx.net" target="_blank" rel="noopener noreferrer" className="text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] hover:underline">atlanticwave-sdx.net</a></span>
                </p>
                <p className="text-sm flex items-center gap-2">
                  <Github className="w-4 h-4 text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]" />
                  <span><span className="font-medium text-foreground">GitHub: </span><a href="https://github.com/atlanticwave-sdx" target="_blank" rel="noopener noreferrer" className="text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] hover:underline">atlanticwave-sdx</a></span>
                </p>
              </div>
            </div>

          {/* Feedback Form */}
          <div className="p-6 bg-white dark:bg-gray-800 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md">
            <h3 className="text-base font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide mb-4">
              Send Feedback
            </h3>
            <form
              onSubmit={(e) => {
                e.preventDefault();
                const form = e.target as HTMLFormElement;
                const name = (form.elements.namedItem("name") as HTMLInputElement).value;
                const email = (form.elements.namedItem("email") as HTMLInputElement).value;
                const subject = (form.elements.namedItem("subject") as HTMLInputElement).value;
                const message = (form.elements.namedItem("message") as HTMLTextAreaElement).value;
                const mailtoLink = `mailto:sdx-support@renci.org?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\n${message}`)}`;
                window.open(mailtoLink, "_blank");
                toast.success("Opening your email client...");
              }}
              className="space-y-4"
            >
              <div className="flex flex-col gap-1">
                <label className="text-xs text-muted-foreground">Name</label>
                <input
                  name="name"
                  type="text"
                  required
                  className="w-full px-3 py-2 text-sm rounded-lg border-2 border-[rgb(200,220,240)] dark:border-blue-500/30 bg-white dark:bg-blue-500/5 focus:outline-none focus:border-[rgb(50,135,200)] dark:focus:border-blue-400 transition-colors"
                  placeholder="Your name"
                />
              </div>
              <div className="flex flex-col gap-1">
                <label className="text-xs text-muted-foreground">Email</label>
                <input
                  name="email"
                  type="email"
                  required
                  className="w-full px-3 py-2 text-sm rounded-lg border-2 border-[rgb(200,220,240)] dark:border-blue-500/30 bg-white dark:bg-blue-500/5 focus:outline-none focus:border-[rgb(50,135,200)] dark:focus:border-blue-400 transition-colors"
                  placeholder="your@email.com"
                />
              </div>
              <div className="flex flex-col gap-1">
                <label className="text-xs text-muted-foreground">Subject</label>
                <input
                  name="subject"
                  type="text"
                  required
                  className="w-full px-3 py-2 text-sm rounded-lg border-2 border-[rgb(200,220,240)] dark:border-blue-500/30 bg-white dark:bg-blue-500/5 focus:outline-none focus:border-[rgb(50,135,200)] dark:focus:border-blue-400 transition-colors"
                  placeholder="Subject"
                />
              </div>
              <div className="flex flex-col gap-1">
                <label className="text-xs text-muted-foreground">Message</label>
                <textarea
                  name="message"
                  required
                  rows={5}
                  className="w-full px-3 py-2 text-sm rounded-lg border-2 border-[rgb(200,220,240)] dark:border-blue-500/30 bg-white dark:bg-blue-500/5 focus:outline-none focus:border-[rgb(50,135,200)] dark:focus:border-blue-400 transition-colors resize-none"
                  placeholder="Your message or feedback..."
                />
              </div>
              <Button
                type="submit"
                className="w-full bg-[rgb(50,135,200)] hover:bg-[rgb(40,115,175)] text-white dark:bg-blue-600 dark:hover:bg-blue-700 transition-colors"
              >
                Send Feedback
              </Button>
            </form>
          </div>
        </div>
      </main>
    </div>
  );
}
