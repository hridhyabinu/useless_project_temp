<!DOCTYPE html>
<html lang="ml">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mukham Nokkum Yenthram (മുഖം നോക്കും യന്ത്രം)</title>
    
    <script src="https://cdn.tailwindcss.com"></script>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">

    <style>
        body {
            font-family: 'JetBrains Mono', monospace;
            background-color: #e0f2fe;
            background-image: linear-gradient(#93c5fd 1px, transparent 1px), linear-gradient(90deg, #93c5fd 1px, transparent 1px);
            background-size: 24px 24px;
        }
        .font-serif-header {
            font-family: 'Cormorant Garamond', serif;
        }
    </style>
</head>
<body class="min-h-screen text-slate-900 flex flex-col justify-between p-4 md:p-8">

    <div id="intro-modal" class="fixed inset-0 bg-slate-950/85 backdrop-blur-sm z-50 flex items-center justify-center p-4">
        <div class="bg-[#e0f2fe] border-2 border-slate-900 p-6 md:p-8 max-w-xl w-full text-center shadow-[8px_8px_0px_0px_rgba(15,23,42,1)] rounded-none">
            <h2 class="font-serif-header text-3xl md:text-4xl font-bold tracking-tight mb-1 text-slate-900">
                മുഖം നോക്കും യന്ത്രം
            </h2>
            <p class="text-xs font-mono uppercase tracking-widest text-slate-600 mb-4">
                Automated Face-Looking Machine v1.0
            </p>

            <div class="border-2 border-slate-900 bg-black mb-6 overflow-hidden aspect-video shadow-[4px_4px_0px_0px_rgba(15,23,42,1)] relative flex items-center justify-center">
                <video id="intro-video" 
                       class="w-full h-full object-cover" 
                       autoplay 
                       loop 
                       muted 
                       playsinline>
                    <source src="/stream-video/intro.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>

            <p class="text-xs text-slate-700 mb-6 leading-relaxed font-mono">
                Optical sensors ready. Click below to un-mute intro video audio and engage Mukham
