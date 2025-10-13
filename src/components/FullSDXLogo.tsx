import sdxLogo from "@/assets/images/sdx-logo.svg";

export function FullSDXLogo() {
  return (
    <div className="text-center space-y-4">
      <div className="flex flex-col items-center space-y-6">
        {/* Title and Logo in same line */}
        <div className="text-center space-y-4 mb-12">
          <div className="flex items-center justify-center gap-4">
            <img
              src={sdxLogo}
              alt="SDX Logo"
              className="h-[110px] w-[110px] object-contain"
            />
            <div className="text-left">
              <h1 className="text-4xl tracking-tight leading-tight font-serif">
                <span className="text-sky-500 font-extrabold">Atlantic</span>
                <span className="text-blue-800">Wave </span>
                <span className="inline-block bg-sky-400 text-white rounded-md pl-[4px] pr-[10px] pt-[8px] text-xl font-serif tracking-wide text-superbold">
                  SDX
                </span>
              </h1>
              <h2 className="text-xs uppercase tracking-tight leading-tight text-blue-800 mt-[-6px]">
                International Distributed Software-Defined Exchange
              </h2>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
